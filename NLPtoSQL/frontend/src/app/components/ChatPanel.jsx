"use client";

import { useState, useRef, useEffect, useContext } from "react";
import { Send, Loader } from "lucide-react";
import ChatMessage from "./ChatMessage";
import { useApi } from "../hooks/useApi";
import { ThemeContext } from "../ThemeContext";
import { useRouter } from "next/navigation";

export default function ChatPanel({ onQueryReceived, onReexecute, onNewChat, initialChats = [] }) {
  const { isDark } = useContext(ThemeContext);
  const router = useRouter();
  const [messages, setMessages] = useState(initialChats);
  const [input, setInput] = useState("");
  const [localLoading, setLocalLoading] = useState(false);
  const scrollRef = useRef(null);
  const textareaRef = useRef(null);
  const { query, loading } = useApi();

  useEffect(() => {
    setMessages(initialChats);
  }, [initialChats]);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || localLoading) return;

    const userQuestion = input.trim();
    setInput("");
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
    setLocalLoading(true);

    try {
      const response = await query(userQuestion);
      const newMessage = {
        question: userQuestion,
        intent: response.intent,
        sql_query: response.sql_query,
        response: response.response,
        filtered_tables: response.filtered_tables,
      };
      setMessages((prev) => [...prev, newMessage]);
      if (onNewChat) {
        onNewChat(newMessage);
      }
      onQueryReceived(
        response.intent === "sql_query" ? response.sql_query : null
      );
    } catch (err) {
      console.error("Query error:", err);
      if (err.response?.status === 503) {
        alert("No database connected");
        setTimeout(() => router.push("/dashboard"), 1000);
      }
    } finally {
      setLocalLoading(false);
    }
  };

  const handleReexecute = (message) => {
    onReexecute(message.sql_query);
  };

  return (
    <div
      className={`flex h-full flex-col ${isDark ? "bg-gray-950" : "bg-white"}`}
    >
      <div className="flex-1 overflow-y-auto space-y-4 p-4 sm:p-6">
        {messages.length === 0 ? (
          <div className="flex h-full items-center justify-center text-center">
            <div>
              <p
                className={`text-lg font-semibold ${
                  isDark ? "text-white" : "text-gray-600"
                }`}
              >
                Welcome to NLP → SQL Studio
              </p>
              <p
                className={`mt-2 text-sm ${
                  isDark ? "text-gray-400" : "text-gray-500"
                }`}
              >
                Ask a natural language question about your data
              </p>
            </div>
          </div>
        ) : (
          <>
            {messages.map((msg, idx) => (
              <ChatMessage
                key={idx}
                message={msg}
                onReexecute={handleReexecute}
              />
            ))}
            <div ref={scrollRef} />
          </>
        )}
      </div>

      <div
        className={`border-t p-4 sm:p-6 w-full ${
          isDark ? "border-gray-800 bg-gray-950" : "border-gray-200 bg-white"
        }`}
      >
        <form onSubmit={handleSubmit} className="flex gap-2 w-full items-end">
          <textarea
            ref={textareaRef}
            value={input}
            onChange={(e) => {
              setInput(e.target.value);
              e.target.style.height = 'auto';
              e.target.style.height = Math.min(e.target.scrollHeight, 200) + 'px';
            }}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSubmit(e);
              }
            }}
            placeholder="Ask a question..."
            disabled={localLoading || loading}
            rows={1}
            className={`flex-1 rounded-lg border px-4 py-2 text-sm placeholder-gray-500 focus:border-blue-500 focus:outline-none disabled:opacity-50 resize-none overflow-y-auto ${
              isDark
                ? "border-gray-600 bg-gray-900 text-white"
                : "border-gray-300 bg-white text-gray-900"
            }`}
          />
          <button
            type="submit"
            disabled={localLoading || loading || !input.trim()}
            className={`flex items-center gap-2 rounded-lg px-4 py-2 font-medium text-white transition-colors  ${
              isDark
                ? "bg-blue-700 hover:bg-blue-800"
                : "bg-blue-700 hover:bg-blue-800"
            }`}
          >
            {localLoading || loading ? (
              <Loader size={18} className="animate-spin" />
            ) : (
              <Send size={18} />
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
