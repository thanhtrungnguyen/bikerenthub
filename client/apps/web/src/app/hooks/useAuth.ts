import { useContext, useDebugValue } from 'react';
import AuthContext, { AuthContextType } from '../context/AuthProvider';

const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  const { auth } = context as AuthContextType;
  useDebugValue(auth, (auth) => (auth?.user ? 'Logged In' : 'Logged Out'));
  return context;
};

export default useAuth;
