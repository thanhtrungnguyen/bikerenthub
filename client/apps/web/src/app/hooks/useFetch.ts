import { useEffect, useState } from 'react';
import useAxiosPrivate from '../hooks/useAxiosPrivate';

export const useFetch = (url: string) => {
  const axios = useAxiosPrivate();
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState();
  const [error, setError] = useState();

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true);
    axios
      .get(url, { signal: controller.signal })
      .then((res) => {
        setData(res.data);
      })
      .catch((err) => setError(err))
      .finally(() => {
        setLoading(false);
      });
    return () => {
      controller.abort();
    };
  }, [url]);

  return { loading, data, error };
};
