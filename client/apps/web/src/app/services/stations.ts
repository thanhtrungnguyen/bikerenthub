import { apiUrl } from "../../environment/apiurl";
import { Station } from "../models/station";

export class StationService {
  constructor(private baseUrl: string = `${apiUrl}/stations`) { }

  async getStations(): Promise<Station[]> {
    const response = await fetch(this.baseUrl, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include', // send cookies
    });

    if (!response.ok) {
      if (response.status === 403) {
        window.location.href = '/login';
        return [];
      }
      throw new Error('Failed to fetch stations');
    }
    return response.json();
  }

  async getStationById(id: number | string): Promise<Station> {
    const response = await fetch(`${this.baseUrl}/${id}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
    });

    if (!response.ok) {
      if (response.status === 403) {
        window.location.href = '/login';
        return {} as Station;
      }
      throw new Error('Failed to fetch station data');
    }
    return response.json();
  }
}
