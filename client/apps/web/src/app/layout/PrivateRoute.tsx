import { Navigate } from 'react-router-dom';
import useAuth from '../hooks/useAuth';

function PrivateRoute({ children }: { children: JSX.Element }) {
  const { auth } = useAuth();

  if (!auth?.user) {
    return <Navigate to="/login" />;
  }

  return children;
}

export default PrivateRoute;