import axios from 'axios'
import { apiUrl } from '../../environment/apiurl';

export const BASE_URL: string = apiUrl || "";

export default axios.create({
  baseURL: `${BASE_URL}/api`,
});

export const axiosPrivate = axios.create({
  baseURL: `${BASE_URL}/api`,
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});
