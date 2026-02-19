"use client";

import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import { PanelGroup, Panel, PanelResizeHandle } from "react-resizable-panels";
import Navbar from "../components/Navbar";
import ChatPanel from "../components/ChatPanel";
import TabbedResultChartPanel from "../components/TabbedResultChartPanel";
import ChartPanel from "../components/ChartPanel";
import SaveDashboardModal from "../components/SaveDashboardModal";
import { useAuth } from "../contexts/AuthContext";
import api from "../../lib/api";

export default function StudioPage() {
  const searchParams = useSearchParams();
  const dbId = searchParams.get("db_id");
  const dashboardId = searchParams.get("dashboard_id");
  const { client } = useAuth();
  
  const [currentSqlQuery, setCurrentSqlQuery] = useState(null);
  const [resultData, setResultData] = useState(null);
  const [charts, setCharts] = useState([]);
  const [activeChartId, setActiveChartId] = useState(null);
  const [chats, setChats] = useState([]);
  const [databaseName, setDatabaseName] = useState("");
  const [dashboardTitle, setDashboardTitle] = useState("");
  const [showSaveModal, setShowSaveModal] = useState(false);

  const handleNewChat = (chat) => {
    setChats(prev => [...prev, chat]);
  };

  const handleResultData = (data) => {
    setResultData(data);
  };

  const handleSelectChart = (chartId) => {
    setActiveChartId(chartId);
  };

  const handleAddChart = (chart) => {
    setCharts([...charts, chart]);
  };

  const handleDeleteChart = (chartId) => {
    setCharts(charts.filter((c) => c.id !== chartId));
  };

  const handleSaveDashboard = async (title) => {
    try {
      const payload = {
        client_id: client?.id,
        db_id: parseInt(dbId),
        chats: chats,
        charts: charts,
        title: title
      };
      
      if (dashboardId && dashboardTitle) {
        const id = dashboardId || searchParams.get("id");
        await api.put(`/dashboards/${id}`, payload);
        alert("Changes saved successfully!");
      } else {
        await api.post("/dashboards", payload);
        alert("Dashboard saved successfully!");
      }
      setDashboardTitle(title);
      setShowSaveModal(false);
    } catch (err) {
      console.error("Failed to save dashboard:", err);
      alert("Failed to save dashboard");
    }
  };

  useEffect(() => {
    if (dashboardId) {
      loadDashboard();
    }
    if (dbId) {
      fetchDatabaseName();
    }
  }, [dashboardId, dbId]);

  const fetchDatabaseName = async () => {
    try {
      const res = await api.get(`/databases/${dbId}`);
      setDatabaseName(res.data.db_name);
    } catch (err) {
      console.error("Failed to fetch database name:", err);
    }
  };

  const loadDashboard = async () => {
    try {
      const res = await api.get(`/dashboards/${dashboardId}`);
      setCharts(res.data.charts || []);
      setChats(res.data.chats || []);
      setDashboardTitle(res.data.title || "");
    } catch (err) {
      console.error("Failed to load dashboard:", err);
    }
  };

  return (
    <div className="flex h-screen flex-col bg-white dark:bg-gray-950">
      <Navbar 
        onSaveDashboard={() => dashboardTitle ? handleSaveDashboard(dashboardTitle) : setShowSaveModal(true)} 
        databaseName={databaseName}
        dashboardTitle={dashboardTitle}
        isExisting={!!dashboardTitle}
      />
      <SaveDashboardModal
        isOpen={showSaveModal}
        onClose={() => setShowSaveModal(false)}
        onSave={handleSaveDashboard}
        currentTitle={dashboardTitle}
      />

      <div className="flex-1 overflow-hidden">
        <PanelGroup direction="horizontal">
          <Panel defaultSize={25} minSize={10}>
            <ChatPanel
              onQueryReceived={setCurrentSqlQuery}
              onReexecute={setCurrentSqlQuery}
              onNewChat={handleNewChat}
              initialChats={chats}
            />
          </Panel>

          <PanelResizeHandle className="w-0.5 bg-gray-200 hover:bg-gray-400 dark:bg-gray-700 dark:hover:bg-gray-600" />

          <Panel defaultSize={50} minSize={20}>
            <TabbedResultChartPanel
              sqlQuery={currentSqlQuery}
              charts={charts}
              onDeleteChart={handleDeleteChart}
              onResultData={handleResultData}
              activeChartId={activeChartId}
              onTabChange={setActiveChartId}
            />
          </Panel>

          <PanelResizeHandle className="w-0.5 bg-gray-200 hover:bg-gray-400 dark:bg-gray-700 dark:hover:bg-gray-600" />

          <Panel defaultSize={25} minSize={20}>
            <ChartPanel 
              resultData={resultData} 
              onAddChart={handleAddChart}
              charts={charts}
              onSelectChart={handleSelectChart}
            />
          </Panel>
        </PanelGroup>
      </div>
    </div>
  );
}
