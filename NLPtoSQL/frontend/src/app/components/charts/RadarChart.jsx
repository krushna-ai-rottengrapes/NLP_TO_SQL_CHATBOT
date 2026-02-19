"use client";

import { Radar } from "react-chartjs-2";
import { Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend } from "chart.js";

ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

export default function RadarChart({ data, isDark }) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "top", labels: { color: isDark ? "#e5e7eb" : "#374151" } },
    },
    scales: {
      r: {
        ticks: { color: isDark ? "#9ca3af" : "#6b7280" },
        grid: { color: isDark ? "#374151" : "#e5e7eb" },
        pointLabels: { color: isDark ? "#9ca3af" : "#6b7280" },
      },
    },
  };

  return (
    <div className="h-full w-full">
      <Radar data={data} options={options} />
    </div>
  );
}
