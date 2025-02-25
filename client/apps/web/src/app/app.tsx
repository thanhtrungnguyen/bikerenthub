import React, { useState } from 'react';
import { BicycleTable } from './bicycle-table';
import { UserDetail } from './user-detail';

interface User {
  username: string;
  phoneNumber: string;
  email: string;
  profileImage: string;
}

export function App() {
  // State to track the currently selected user (if any)
  const [selectedUser, setSelectedUser] = useState<User | null>(null);

  // Callback to be passed to the BicycleTable
  const handleUserClick = (user: User) => {
    // Toggle the detail view: collapse if already selected, or expand otherwise.
    if (selectedUser && selectedUser.username === user.username) {
      setSelectedUser(null);
    } else {
      setSelectedUser(user);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Dashboard</h1>
      <BicycleTable onUserClick={handleUserClick} />
      {selectedUser && (
        <div className="mt-4">
          <UserDetail user={selectedUser} />
        </div>
      )}
    </div>
  );
}

export default App;
