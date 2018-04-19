module TuningCurvePortal
using MAT
using DataFrames
using CSV
using Query
using Plots


"""
plot spike raster.

plotSpikeTrain(spiketrain; xrange=(0,360), imgsize=(1000,500))
spiketrain::[(name, times::Array)]
"""
function plotSpikeTrain(spiketrain::Array{Tuple{String, Array{Float64, 2}}, 1};
                        xrange=(0,360), imgsize=(1000,500))
    plot()
    n, = size(spiketrain)
    for each_train = 1:n
        for item in [point for point in spiketrain[each_train][2] if xrange[1] <= point <= xrange[2]]
            plot!([item,item],[each_train-1,each_train], color = :blue)
        end
    end
    plot!(legend=false, size=imgsize, xlim=xrange)
end


"""
get the data of the test subject.

getTargetData(target; data_dir="NEX_TRAIN")::(spike_trains, marker, stim_info)
"""
function getTargetData(target; data_dir="data/NEX_TRAIN")
    spike_train_pool = matread(joinpath(data_dir, target * ".mat"))
    unit_names = [item[1] for item in spike_train_pool if item[1] != "DIG01"]
    spike_trains = [(name, spike_train_pool[name]["times"])
                    for name in unit_names]
    marker = spike_train_pool["DIG01"]["times"]

    stim_info_raw = CSV.read(joinpath(data_dir, target * ".csv"),
                             nullable=false)
    stim_info = @from item in stim_info_raw begin
                @where item.colorname != "START" && item.colorname != "QUIT"
                @select (item.startstamp, item.colorname)
                @collect
    end

    return (spike_trains, marker, stim_info)
end


"""
the linear filter kernel.

we are using guassian kernel:

``w(\\tau) = \\frac{1}{\\sigma_w \\sqrt{2 \\pi}}
\\exp(- \\frac{\\tau^2}{2 \\sigma_w^2})``

"""
function kernel_w(t, sigma_w = 0.4)
    exp.(- t.*t / (2 * sigma_w * sigma_w)) / (sqrt(2 * pi) * sigma_w)
end


"""
generate the response function with guassian kernel_w.

return Array{Tuple{String, Func},1}.
"""
function trimIntoAverageFiringRate(single_train, marker, stim_info; ROI=(-1,5))
    trials = Dict()
    for idx = 1:min(length(marker),length(stim_info))
        trial_name = stim_info[idx][2]
        trial_mark = marker[idx]

        trial_spike = [item - trial_mark
                       for item in single_train
                       if ROI[1] < item - trial_mark <= ROI[2]]
        length(trial_spike) == 0?trial_spike=[-999]:nothing

        trial_filter = t -> sum(kernel_w(t - trial_spike))

        if !haskey(trials, trial_name)
            trials[trial_name] = [trial_filter]
        else
            trials[trial_name] = vcat(trials[trial_name], [trial_filter])
        end
    end

    trials_mean = []
    for (key, funcs) in trials
        n = length(funcs)
        trials_mean = vcat(trials_mean,
                           (key, t -> sum(map(fun -> fun(t), funcs)) / n)
                          )
    end
    sort!(trials_mean, by=x->x[1])
    return trials_mean
end


function getColorLuminanceValue(nametag, namestring; sep="#")
    if nametag in [:green, :blue]
        parse(namestring[2:end]) |> Int
    else
        parse.(split(namestring[2:end], sep)) |> Tuple
    end
end


"""
generate the data point for tuning curve.
ie. find the max value of each response curve.

returns Array{Tuple{String, Int|Tuple{Int, Int}, Float64}, 1}.
"""
function getTuningCurve(trials_mean)
    colornames = Dict("B"=>:blue, "G"=>:green, "L"=>:luminance)
    colortag = colornames[trials_mean[1][1][1:1]]

    [(colornames[name[1:1]],
      getColorLuminanceValue(colornames[name[1:1]], name),
      findmax(func.(-1:0.01:5))[1])
    for (name, func) in trials_mean]
end

end  # module SpikeTrainPortal
