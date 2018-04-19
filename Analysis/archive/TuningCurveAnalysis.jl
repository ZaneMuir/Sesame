using Plots
include("TuningCurvePortal.jl");
include("TuningCurvePlot.jl");

target_name = "ts6_SC_180401_GBL"
(spike_trains, marker, stim_info) = TuningCurvePortal.getTargetData(target_name)

responses = [(name, TuningCurvePortal.trimIntoAverageFiringRate(train, marker, stim_info))
             for (name, train) in spike_trains]
tuningcurve_set = [(name, TuningCurvePortal.getTuningCurve(response_set))
                   for (name, response_set) in responses]


chart_dir = joinpath("data/CHART",target_name)
isdir(chart_dir)?nothing:mkdir(chart_dir)

for idx = 1:length(spike_trains)
    unit_response = responses[idx][2]
    unit_tuningcurve = tuningcurve_set[idx][2]

    # GB plot
    plot()
    plot_green = TuningCurvePlot.plotResponseOfTrial(unit_response, unit_tuningcurve, :greens, palette=:greens, name="greens")
    plot_blue  = TuningCurvePlot.plotResponseOfTrial(unit_response, unit_tuningcurve, :blues, palette=:blues, name="blues")
    tplot_green = TuningCurvePlot.plotTuningCurveScatter(unit_tuningcurve, [:green], name="greens")
    tplot_breen = TuningCurvePlot.plotTuningCurveScatter(unit_tuningcurve, [:blue], name="blues")

    a = plot(plot_green, plot_blue, layout=(2,1), size=(1000,1000))
    b = plot(tplot_green, tplot_breen, layout=(2,1), size=(1000,1000))
    x = plot(a, b, size=(1500,1200))
    #savefig(joinpath(chart_dir, target_name*"_"*responses[idx][1]*"_GBcurve.png"))

    # L plot
    plot()
    cg = TuningCurvePlot.collapseHeatMap(unit_tuningcurve,2,color=:green, name="L-greens")
    cb = TuningCurvePlot.collapseHeatMap(unit_tuningcurve,1,color=:blue, name="L-blues")
    ht = TuningCurvePlot.plotTuningHeatMap(unit_tuningcurve)
    ht2 = TuningCurvePlot.plotTuningHeatMap(unit_tuningcurve)

    a = plot(cg, cb, layout=(2,1))
    b = plot(ht, ht2, layout=(2,1))
    y = plot(a,b, size=(1000,1000))
    #savefig(joinpath(chart_dir, target_name*"_"*responses[idx][1]*"_tuningcv.png"))

    # combine and export
    plot(x,y,size=(2000,1000))
    savefig(joinpath(chart_dir, target_name*"_"*responses[idx][1]*"_summary_0_4.png"))
end
