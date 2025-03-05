import React from 'react';

interface Bicycle {
  id: string;
  status: 'booked' | 'available' | 'lost';
  startTime?: string;
  endTime?: string;
  bookingUser?: string;
}

// Dummy bicycle data
const dummyBicycles: Bicycle[] = [
  { id: 'BIC001', status: 'available' },
  {
    id: 'BIC002',
    status: 'booked',
    startTime: '10:00 AM',
    endTime: '10:45 AM',
    bookingUser: 'Alice',
  },
  { id: 'BIC003', status: 'lost' },
];

interface BicycleTableProps {
  onUserClick: (user: {
    username: string;
    phoneNumber: string;
    email: string;
    profileImage: string;
  }) => void;
}

export function BicycleTable({ onUserClick }: BicycleTableProps) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full border-collapse border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="border border-gray-300 px-4 py-2">ID Tag</th>
            <th className="border border-gray-300 px-4 py-2">Status</th>
            <th className="border border-gray-300 px-4 py-2">Allotted Time</th>
            <th className="border border-gray-300 px-4 py-2">Booking User</th>
          </tr>
        </thead>
        <tbody>
          {dummyBicycles.map((bicycle) => (
            <tr key={bicycle.id} className="text-center">
              <td className="border border-gray-300 px-4 py-2">{bicycle.id}</td>
              <td className="border border-gray-300 px-4 py-2">
                {bicycle.status}
              </td>
              <td className="border border-gray-300 px-4 py-2">
                {bicycle.status === 'booked'
                  ? `${bicycle.startTime || '-'} - ${bicycle.endTime || '-'}`
                  : '-'}
              </td>
              <td className="border border-gray-300 px-4 py-2">
                {bicycle.status === 'booked' ? (
                  <button
                    type="button"
                    className="text-blue-600 hover:underline focus:outline-none"
                    onClick={() =>
                      onUserClick({
                        username: bicycle.bookingUser || 'Unknown',
                        phoneNumber: '123-456-7890', // Dummy data for demonstration
                        email: 'alice@example.com', // Dummy data for demonstration
                        profileImage: 'https://via.placeholder.com/150',
                      })
                    }
                  >
                    {bicycle.bookingUser}
                  </button>
                ) : (
                  '-'
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
