"use client";

import { createContext, useState, useEffect, useContext } from "react";
import { clearTokenCache } from "../../lib/api.js";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [client, setClient] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch('/api/auth/me');
        if (response.ok) {
          const { user: userData, client: clientData } = await response.json();
          setUser(userData);
          setClient(clientData);
        }
      } catch (error) {
        console.error('Failed to fetch user:', error);
      }
      setLoading(false);
    };
    
    fetchUser();
  }, []);

  const login = async (username, password) => {
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        const error = await response.json();
        return { success: false, error: error.error || "Login failed" };
      }

      const { user: userData, client: clientData } = await response.json();
      clearTokenCache();
      setUser(userData);
      setClient(clientData);
      return { success: true };
    } catch (error) {
      return { success: false, error: "Login failed" };
    }
  };

  const logout = async () => {
    await fetch('/api/auth/logout', { method: 'POST' });
    clearTokenCache();
    setUser(null);
    setClient(null);
  };

  const isOwner = () => user?.role === "internal_superuser" || user?.role === "client";
  const isViewer = () => user?.role === "client_user";

  return (
    <AuthContext.Provider value={{ user, client, login, logout, loading, isOwner, isViewer }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
