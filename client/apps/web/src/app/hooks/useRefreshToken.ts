import axios from '../api/axios';
import useAuth from './useAuth';
import { AuthContextType } from '../context/AuthProvider';

const useRefreshToken = () => {
  const { setAuth } = useAuth() as AuthContextType;

  const refresh = async () => {
    const response = await axios.get('/auth/refresh', {
      withCredentials: true,
    });
    setAuth((prev: { user: unknown; accessToken: string }) => {
      return {
        ...prev,
        accessToken: response.data.accessToken,
        user: response.data.user,
      };
    });
    return response.data.accessToken;
  };

  return refresh;
};

export default useRefreshToken;
