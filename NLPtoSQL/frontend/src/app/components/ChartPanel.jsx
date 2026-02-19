"use client";

import { useState, useContext } from "react";
import { ThemeContext } from "../ThemeContext";
import {
  BarChart3,
  LineChart as LineIcon,
  PieChart,
  TrendingUp,
  Activity,
  Layers,
} from "lucide-react";
import dynamic from "next/dynamic";

const LineChart = dynamic(() => import("./charts/LineChart"), { ssr: false });
const BarChart = dynamic(() => import("./charts/BarChart"), { ssr: false });
const HorizontalBarChart = dynamic(
  () => import("./charts/HorizontalBarChart"),
  { ssr: false }
);
const PieChartComponent = dynamic(() => import("./charts/PieChartComponent"), {
  ssr: false,
});
const DoughnutChart = dynamic(() => import("./charts/DoughnutChart"), {
  ssr: false,
});
const AreaChart = dynamic(() => import("./charts/AreaChart"), { ssr: false });
const RadarChart = dynamic(() => import("./charts/RadarChart"), { ssr: false });

const CHART_TYPES = [
  {
    id: "line",
    name: "Line Chart",
    icon: LineIcon,
    component: LineChart,
    hasAxis: true,
  },
  {
    id: "bar",
    name: "Bar Chart",
    icon: BarChart3,
    component: BarChart,
    hasAxis: true,
  },
  {
    id: "horizontalBar",
    name: "Horizontal Bar",
    icon: TrendingUp,
    component: HorizontalBarChart,
    hasAxis: true,
  },
  {
    id: "pie",
    name: "Pie Chart",
    icon: PieChart,
    component: PieChartComponent,
    hasAxis: false,
  },
  {
    id: "doughnut",
    name: "Doughnut",
    icon: Activity,
    component: DoughnutChart,
    hasAxis: false,
  },
  {
    id: "area",
    name: "Area Chart",
    icon: Layers,
    component: AreaChart,
    hasAxis: true,
  },
  {
    id: "radar",
    name: "Radar Chart",
    icon: Activity,
    component: RadarChart,
    hasAxis: true,
  },
];

export default function ChartPanel({ resultData, onAddChart, charts, onSelectChart }) {
  const { isDark } = useContext(ThemeContext);
  const [selectedChart, setSelectedChart] = useState(null);
  const [showColumnSelector, setShowColumnSelector] = useState(false);
  const [chartConfig, setChartConfig] = useState({
    title: "",
    category: "",
    values: [],
  });
  // console.log("resultData", resultData);
  let hasTableData = false;
  let tableData = [];

  if (resultData?.tables && resultData.tables.length > 0) {
    hasTableData = true;
    tableData = resultData.tables[0].data;
  } else if (resultData?.data && resultData.data.length > 0) {
    hasTableData = true;
    tableData = resultData.data;
  }

  // console.log("Table Data-> ",tableData)

  const availableColumns =
    tableData.length > 0 ? Object.keys(tableData[0]) : [];

  const handleChartClick = (chartType) => {
    setSelectedChart(chartType);
    setShowColumnSelector(true);
    setChartConfig({ title: "", category: "", values: [] });
  };

  const handleGenerateChart = () => {
    if (
      !chartConfig.title ||
      !chartConfig.category ||
      chartConfig.values.length === 0
    )
      return;

    const labels = tableData.map((row) => String(row[chartConfig.category]));
    const datasets = chartConfig.values.map((col, idx) => ({
      label: col,
      data: tableData.map((row) => {
        const val = row[col];
        // return typeof val === "number" ? val : parseFloat(val) || 0;
        return String(val)
      }),
      backgroundColor: `hsla(${idx * 60}, 70%, 60%, 0.6)`,
      borderColor: `hsla(${idx * 60}, 70%, 60%, 1)`,
      borderWidth: 2,
    }));

    const newChart = {
      id: Date.now(),
      title: chartConfig.title,
      type: selectedChart,
      data: { labels, datasets },
    };

    if (onAddChart) {
      onAddChart(newChart);
    }
    setShowColumnSelector(false);
    setSelectedChart(null);
    setChartConfig({ title: "", category: "", values: [] });
  };

  const categoryLabel = selectedChart?.hasAxis
    ? "Category (X-Axis)"
    : "Category";
  const valuesLabel = selectedChart?.hasAxis ? "Values (Y-Axis)" : "Values";

  return (
    <div
      className={`h-full flex flex-col ${isDark ? "bg-gray-950" : "bg-white"}`}
    >
      <div
        className={`border-b p-4 ${
          isDark ? "border-gray-800" : "border-gray-200"
        }`}
      >
        <h3
          className={`text-lg font-semibold mb-3 ${
            isDark ? "text-white" : "text-gray-900"
          }`}
        >
          Charts
        </h3>

        <div className="grid grid-cols-1 xl:grid-cols-2 gap-2">
          {CHART_TYPES.map((chart) => {
            const Icon = chart.icon;
            return (
              <button
                key={chart.id}
                onClick={() => handleChartClick(chart)}
                disabled={!hasTableData}
                className={`flex items-center gap-2 rounded-lg border px-3 py-2 text-sm transition-colors ${
                  !hasTableData
                    ? "cursor-not-allowed opacity-40"
                    : selectedChart?.id === chart.id
                    ? "border-blue-600 bg-blue-50 text-blue-600 dark:bg-blue-900/20"
                    : isDark
                    ? "border-gray-700 hover:bg-gray-800 text-gray-300"
                    : "border-gray-300 hover:bg-gray-50 text-gray-700"
                }`}
              >
                <Icon size={16} />
                {chart.name}
              </button>
            );
          })}
        </div>
      </div>

      {showColumnSelector && (
        <div
          className={`border-b p-4 ${
            isDark ? "border-gray-800" : "border-gray-200"
          } overflow-y-scroll`}
        >
          <h4
            className={`text-sm font-semibold mb-3 ${
              isDark ? "text-white" : "text-gray-900"
            }`}
          >
            Configure Chart
          </h4>

          <div className="space-y-3 ">
            <div>
              <label
                className={`block text-sm mb-1 ${
                  isDark ? "text-gray-300" : "text-gray-700"
                }`}
              >
                Chart Title
              </label>
              <input
                type="text"
                value={chartConfig.title}
                onChange={(e) =>
                  setChartConfig({ ...chartConfig, title: e.target.value })
                }
                placeholder="Enter chart title"
                className={`w-full rounded border px-3 py-2 text-sm ${
                  isDark
                    ? "border-gray-700 bg-gray-800 text-white placeholder-gray-500"
                    : "border-gray-300 bg-white text-gray-900 placeholder-gray-400"
                }`}
              />
            </div>

            <div>
              <label
                className={`block text-sm mb-1 ${
                  isDark ? "text-gray-300" : "text-gray-700"
                }`}
              >
                {categoryLabel}
              </label>
              <select
                value={chartConfig.category}
                onChange={(e) =>
                  setChartConfig({ ...chartConfig, category: e.target.value })
                }
                className={`w-full rounded border px-3 py-2 text-sm ${
                  isDark
                    ? "border-gray-700 bg-gray-800 text-white"
                    : "border-gray-300 bg-white text-gray-900"
                }`}
              >
                <option value="">Select...</option>
                {availableColumns.map((col) => (
                  <option key={col} value={col}>
                    {col}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label
                className={`block text-sm mb-1 ${
                  isDark ? "text-gray-300" : "text-gray-700"
                }`}
              >
                {valuesLabel}
              </label>
              <div className="space-y-1 max-h-32 overflow-y-auto">
                {availableColumns.map((col) => (
                  <label key={col} className="flex items-center gap-2 text-sm">
                    <input
                      type="checkbox"
                      checked={chartConfig.values.includes(col)}
                      onChange={(e) => {
                        if (e.target.checked) {
                          setChartConfig({
                            ...chartConfig,
                            values: [...chartConfig.values, col],
                          });
                        } else {
                          setChartConfig({
                            ...chartConfig,
                            values: chartConfig.values.filter((v) => v !== col),
                          });
                        }
                      }}
                      className="rounded"
                    />
                    <span
                      className={isDark ? "text-gray-300" : "text-gray-700"}
                    >
                      {col}
                    </span>
                  </label>
                ))}
              </div>
            </div>

            <button
              onClick={handleGenerateChart}
              disabled={
                !chartConfig.title ||
                !chartConfig.category ||
                chartConfig.values.length === 0
              }
              className="w-full rounded-lg bg-blue-600 px-3 py-2 text-sm text-white hover:bg-blue-700 disabled:opacity-50"
            >
              Create Chart
            </button>
          </div>
        </div>
      )}

      <div className="flex-1 overflow-auto p-4">
        {charts && charts.length > 0 ? (
          <div className="space-y-2">
            <h4 className={`text-sm font-semibold mb-3 ${isDark ? "text-white" : "text-gray-900"}`}>
              Created Charts
            </h4>
            {charts.map((chart) => {
              const chartType = CHART_TYPES.find(c => c.id === chart.type.id);
              const Icon = chartType?.icon || BarChart3;
              return (
                <button
                  key={chart.id}
                  onClick={() => onSelectChart && onSelectChart(chart.id)}
                  className={`w-full flex items-center gap-3 rounded-lg border p-3 text-left transition-colors ${
                    isDark
                      ? "border-gray-700 hover:bg-gray-800 text-gray-300"
                      : "border-gray-300 hover:bg-gray-50 text-gray-700"
                  }`}
                >
                  <Icon size={20} className="text-blue-600" />
                  <div className="flex-1">
                    <p className={`font-medium ${isDark ? "text-white" : "text-gray-900"}`}>
                      {chart.title}
                    </p>
                    <p className={`text-xs ${isDark ? "text-gray-500" : "text-gray-500"}`}>
                      {chartType?.name}
                    </p>
                  </div>
                </button>
              );
            })}
          </div>
        ) : (
          <div className="flex h-full items-center justify-center">
            <p className={`text-sm ${isDark ? "text-gray-400" : "text-gray-600"}`}>
              {!hasTableData
                ? "No table data available for charts"
                : "No charts created yet. Configure and create a chart above."}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
