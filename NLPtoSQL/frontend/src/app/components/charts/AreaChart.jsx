"use client";

import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, Filler } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend, Filler);

export default function AreaChart({ data, isDark }) {
  const areaData = {
    ...data,
    datasets: data.datasets.map(ds => ({ ...ds, fill: true }))
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "top", labels: { color: isDark ? "#e5e7eb" : "#374151" } },
    },
    scales: {
      x: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
      y: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
    },
  };

  return (
    <div className="h-full w-full">
      <Line data={areaData} options={options} />
    </div>
  );
}
