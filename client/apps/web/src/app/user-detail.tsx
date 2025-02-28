interface User {
  username: string;
  phoneNumber: string;
  email: string;
  profileImage: string; // URL to the profile image
}

const dummyUser: User = {
  username: 'johndoe',
  phoneNumber: '123-456-7890',
  email: 'johndoe@example.com',
  profileImage: 'https://via.placeholder.com/150',
};

export function UserDetail({ user = dummyUser }: { user?: User }) {
  return (
    <div className="max-w-sm mx-auto bg-white rounded shadow-lg overflow-hidden">
      <img
        src={user.profileImage}
        alt={`${user.username}'s profile`}
        className="w-full h-48 object-cover"
      />
      <div className="p-4 text-center">
        <h5 className="text-xl font-semibold">{user.username}</h5>
        <p className="text-gray-600">
          <strong>Email:</strong> {user.email}
        </p>
        <p className="text-gray-600">
          <strong>Phone:</strong> {user.phoneNumber}
        </p>
      </div>
    </div>
  );
}

export default UserDetail;
