import { useState, useCallback } from "react";
import api from "../../lib/api.js";

export function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const query = useCallback(async (question) => {
    setLoading(true);
    setError(null);
    try {
      const res = await api.post("/database/query", { question });
      return res.data;
    } catch (err) {
      const errorMsg = err.response?.data?.detail || "Query failed";
      setError(errorMsg);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const executeSql = useCallback(async (sql_query) => {
    setLoading(true);
    setError(null);
    try {
      const res = await api.post("/database/execute-sql", { sql_query });
      return res.data;
    } catch (err) {
      const errorMsg = err.response?.data?.detail || "Execution failed";
      setError(errorMsg);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return { query, executeSql, loading, error };
}
