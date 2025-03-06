// apps/your-app/src/app/components/StationDetail.tsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Station } from '../models/station';
import { Bike } from '../models/bike';
import { BikeService } from '../services/bikes';
import { StationService } from '../services/stations';

const stationService = new StationService();
const bikeService = new BikeService();

const StationDetail: React.FC = () => {
  const { stationId } = useParams<{ stationId: string }>();
  const [station, setStation] = useState<Station | null>(null);
  const [bikes, setBikes] = useState<Bike[]>([]);
  const [error, setError] = useState<string>('');

  // Fetch station details
  useEffect(() => {
    if (stationId) {
      stationService
        .getStationById(stationId)
        .then(setStation)
        .catch((err: Error) => setError(err.message));
    }
  }, [stationId]);

  // Once station is loaded, fetch bikes for that station
  useEffect(() => {
    if (station) {
      bikeService
        .getBikesForStation(station.id)
        .then(setBikes)
        .catch((err: Error) => setError(err.message));
    }
  }, [station]);

  if (error) {
    return <div className="text-red-500 text-center mt-8">{error}</div>;
  }

  if (!station) {
    return <div className="text-center mt-8">Loading station details...</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Station Details</h1>
      <div className="bg-white shadow-lg rounded-lg p-6 mb-8">
        <p className="mb-2">
          <span className="font-semibold">ID:</span> {station.id}
        </p>
        <p className="mb-2">
          <span className="font-semibold">Name:</span> {station.name}
        </p>
        <p className="mb-2">
          <span className="font-semibold">Latitude:</span> {station.latitude}
        </p>
        <p className="mb-2">
          <span className="font-semibold">Longitude:</span> {station.longtitude}
        </p>
        <p className="mb-2">
          <span className="font-semibold">Total Capacity:</span>{' '}
          {station.total_capacity}
        </p>
        <p className="mb-2">
          <span className="font-semibold">Current Bikes:</span>{' '}
          {station.current_bikes}
        </p>
      </div>

      <h2 className="text-2xl font-bold mb-4">Bikes at this Station</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
          <thead className="bg-gray-200">
            <tr>
              <th className="py-3 px-6 text-left">Bike ID</th>
              <th className="py-3 px-6 text-left">Bike Type</th>
              <th className="py-3 px-6 text-left">Status</th>
            </tr>
          </thead>
          <tbody>
            {bikes.map((bike) => (
              <tr key={bike.id} className="border-b hover:bg-gray-50">
                <td className="py-4 px-6">{bike.id}</td>
                <td className="py-4 px-6">{bike.bike_type}</td>
                <td className="py-4 px-6">{bike.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default StationDetail;
