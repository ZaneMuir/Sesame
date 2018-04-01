module TuningCurvePlot

using Plots


function plotResponseOfTrial(source, tuning, targets=:all;
                             imgsize=(1000,500), xrange=(-1,5),
                             palette=:inferno, ymax=20, name="")
    plot(size=imgsize, xlim=xrange, palette=palette)

    if targets == :all
        plot_source = source
    elseif targets == :greens
        plot_source = [item for item in source if startswith(item[1][1:1], "G")]
    elseif targets == :blues
        plot_source = [item for item in source if startswith(item[1][1:1], "B")]
    elseif targets == :luminance
        plot_source = [item for item in source if startswith(item[1][1:1], "L")]
    else
        plot_source = [item for item in source if item[1] in targets]
    end

    for (name, func) in plot_source
        #println(name)
        plot!(func, xrange[1], xrange[2], label=name)
    end
    ymax = max(ymax, findmax([r_max for (name, pos, r_max) in tuning])[1])
    plot!(ylim=(0,ymax), title=name)
end


"""

"""
function plotTuningCurveScatter(source, targets=:all;
                             imgsize=(1000,500), xrange=(-0.5,8.5), ymax=20,
                             palette=:inferno, name="")
    color_map = [:blue, :green]
    if targets == :all
        plot_source = source
    else
        plot_source = [item for item in source if item[1] in targets]
    end

    plot(size=imgsize, xlim=xrange, palette=palette)
    for (name, pos, r_max) in plot_source

        name in color_map?scatter!([pos], [r_max], color=name, ms=10):nothing
    end
    ymax = max(ymax, findmax([r_max for (name, pos, r_max) in plot_source])[1])
    plot!(ylim=(0,ymax), legend=false, title=name)
end


function plotTuningHeatMap(source;
                           imgsize=(550,500),
                           palette=:inferno, name="")
    tuning_map = zeros((8,8))
    for (tag, (pos_x, pos_y), r_max) in [item for item in source if item[1] == :luminance]
        tag == :luminance?tuning_map[pos_x, pos_y] = r_max:nothing
    end
    heatmap(tuning_map, size=imgsize, title=name)
end


function collapseHeatMap(source, axis=1;
                         figsize=(1000,500), color=:black, ymax=20, name="")
    plot_data = zeros(8)
    for (name, pos, r_max) in [item for item in source if item[1] == :luminance]
        plot_data[pos[axis]] += r_max
    end
    plot_data = plot_data / 8
    ymax = max(ymax, findmax(plot_data)[1])
    scatter(1:8, plot_data, ms=10, ylim=(0,ymax),
            size=figsize, color=color, legend=false, title=name)
end

end
