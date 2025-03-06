// apps/your-app/src/app/components/Dashboard.tsx
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { StationService } from '../services/stations';
import { Station } from '../models/station';

const stationService = new StationService();

const Dashboard: React.FC = () => {
  const [stations, setStations] = useState<Station[]>([]);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    stationService.getStations()
      .then(setStations)
      .catch((err: Error) => setError(err.message));
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-6">Bike Stations Dashboard</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
          <thead className="bg-gray-200">
            <tr>
              <th className="py-3 px-6 text-left">ID</th>
              <th className="py-3 px-6 text-left">Name</th>
              <th className="py-3 px-6 text-left">Latitude</th>
              <th className="py-3 px-6 text-left">Longitude</th>
              <th className="py-3 px-6 text-left">Capacity</th>
              <th className="py-3 px-6 text-left">Current Bikes</th>
            </tr>
          </thead>
          <tbody>
            {stations.map((station) => (
              <tr key={station.id} className="border-b hover:bg-gray-50">
                <td className="py-4 px-6">{station.id}</td>
                <td className="py-4 px-6">
                  <Link
                    to={`/stations/${station.id}`}
                    className="text-blue-500 hover:underline"
                  >
                    {station.name}
                  </Link>
                </td>
                <td className="py-4 px-6">{station.latitude}</td>
                <td className="py-4 px-6">{station.longtitude}</td>
                <td className="py-4 px-6">{station.total_capacity}</td>
                <td className="py-4 px-6">{station.current_bikes}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
