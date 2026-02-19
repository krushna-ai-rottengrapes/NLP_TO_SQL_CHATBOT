"use client";

import { useState, useContext, useEffect } from "react";
import { ThemeContext } from "../ThemeContext";
import { Table, X } from "lucide-react";
import ResultPanel from "./ResultPanel";
import dynamic from "next/dynamic";

const LineChart = dynamic(() => import("./charts/LineChart"), { ssr: false });
const BarChart = dynamic(() => import("./charts/BarChart"), { ssr: false });
const HorizontalBarChart = dynamic(() => import("./charts/HorizontalBarChart"), { ssr: false });
const PieChartComponent = dynamic(() => import("./charts/PieChartComponent"), { ssr: false });
const DoughnutChart = dynamic(() => import("./charts/DoughnutChart"), { ssr: false });
const AreaChart = dynamic(() => import("./charts/AreaChart"), { ssr: false });
const RadarChart = dynamic(() => import("./charts/RadarChart"), { ssr: false });

const CHART_COMPONENTS = {
  line: LineChart,
  bar: BarChart,
  horizontalBar: HorizontalBarChart,
  pie: PieChartComponent,
  doughnut: DoughnutChart,
  area: AreaChart,
  radar: RadarChart,
};

export default function TabbedResultChartPanel({ sqlQuery, charts, onDeleteChart, onResultData, activeChartId, onTabChange }) {
  const { isDark } = useContext(ThemeContext);
  const [activeTab, setActiveTab] = useState(activeChartId || "results");
  const [cachedResultData, setCachedResultData] = useState(null);

  useEffect(() => {
    if (activeChartId) {
      setActiveTab(activeChartId);
    }
  }, [activeChartId]);

  const handleResultData = (data) => {
    setCachedResultData(data);
    if (onResultData) {
      onResultData(data);
    }
  };

  return (
    <div className={`h-full flex flex-col ${isDark ? "bg-gray-950" : "bg-white"}`}>
      <div className={`border-b ${isDark ? "border-gray-800" : "border-gray-200"}`}>
        <div className="flex overflow-x-auto scrollbar-thin">
          <button
            onClick={() => {
              setActiveTab("results");
              onTabChange && onTabChange("results");
            }}
            className={`flex items-center gap-2 px-4 py-3 text-sm font-medium border-b-2 transition-colors whitespace-nowrap ${
              activeTab === "results"
                ? isDark
                  ? "border-blue-500 text-blue-400 bg-gray-900"
                  : "border-blue-600 text-blue-600 bg-blue-50"
                : isDark
                ? "border-transparent text-gray-400 hover:text-gray-300 hover:bg-gray-900"
                : "border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50"
            }`}
          >
            <Table size={16} />
            Results
          </button>

          {charts.map((chart) => (
            <button
              key={chart.id}
              onClick={() => {
                setActiveTab(chart.id);
                onTabChange && onTabChange(chart.id);
              }}
              className={`flex items-center gap-2 px-4 py-3 text-sm font-medium border-b-2 transition-colors whitespace-nowrap ${
                activeTab === chart.id
                  ? isDark
                    ? "border-blue-500 text-blue-400 bg-gray-900"
                    : "border-blue-600 text-blue-600 bg-blue-50"
                  : isDark
                  ? "border-transparent text-gray-400 hover:text-gray-300 hover:bg-gray-900"
                  : "border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50"
              }`}
            >
              {chart.title}
              <X
                size={14}
                onClick={(e) => {
                  e.stopPropagation();
                  if (activeTab === chart.id) {
                    setActiveTab("results");
                  }
                  onDeleteChart(chart.id);
                }}
                className="hover:text-red-500"
              />
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-hidden">
        {activeTab === "results" ? (
          <ResultPanel sqlQuery={sqlQuery} onResultData={handleResultData} />
        ) : (
          <div className="h-full p-6 overflow-x-auto">
            {charts
              .filter((c) => c.id === activeTab)
              .map((chart) => {
                const ChartComponent = CHART_COMPONENTS[chart.type.id];
                return (
                  <div key={chart.id} className="h-full min-w-[600px]">
                    <h3 className={`text-xl font-bold mb-4 ${isDark ? "text-white" : "text-gray-900"}`}>
                      {chart.title}
                    </h3>
                    <div className="h-[calc(100%-3rem)]">
                      {ChartComponent && <ChartComponent data={chart.data} isDark={isDark} />}
                    </div>
                  </div>
                );
              })}
          </div>
        )}
      </div>
    </div>
  );
}
