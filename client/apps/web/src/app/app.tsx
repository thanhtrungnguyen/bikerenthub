import { Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import RequireAuth from './pages/AuthFilter';
import Login from './pages/Login';
import StationDetail from './pages/StationDetail';

export function App() {
  return (
    <Routes>
      {/* Redirect the root path to the dashboard if authenticated,
        or to login if not */}
      <Route path="/" element={<Navigate replace to="/dashboard" />} />

      {/* Public route for login */}
      <Route path="/login" element={<Login />} />

      {/* Protected routes */}
      <Route
        path="/dashboard"
        element={
          <RequireAuth>
            <Dashboard />
          </RequireAuth>
        }
      />
      <Route
        path="/stations/:stationId"
        element={
          <RequireAuth>
            <StationDetail />
          </RequireAuth>
        }
      />
    </Routes>
  );
}

export default App;
