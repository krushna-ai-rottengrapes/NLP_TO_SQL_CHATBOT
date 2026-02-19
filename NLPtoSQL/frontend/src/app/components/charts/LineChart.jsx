"use client";

import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function LineChart({ data, isDark }) {
  if (!data) return null;
  // console.log(data)
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "top", labels: { color: isDark ? "#e5e7eb" : "#374151" } },
      title: { display: false },
    },
    scales: {
      x: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
      y: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
    },
  };

  return (
    <div className="h-full w-full">
      <Line data={data} options={options} />
    </div>
  );
}
