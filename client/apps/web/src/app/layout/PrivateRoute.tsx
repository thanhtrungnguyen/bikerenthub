import { Navigate } from 'react-router-dom';
import useAuth from '../hooks/useAuth';

function PrivateRoute({ children }: { children: JSX.Element }) {
  const { auth } = useAuth();

  if (!auth?.user) {
    console.log('PrivateRoute: ', auth);
    return <Navigate to="/login" />;
  }

  return children;
}

export default PrivateRoute;
