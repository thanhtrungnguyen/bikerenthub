import { apiUrl } from "../../environment/apiurl";
import { Station } from "../models/station";

export class StationService {
  constructor(private baseUrl: string = `${apiUrl}/stations`) { }

  private getToken(): string | null {
    return localStorage.getItem('token');
  }

  async getStations(): Promise<Station[]> {
    const token = this.getToken();
    const response = await fetch(this.baseUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
    });

    if (!response.ok) {
      if (response.status === 403 || response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
        return [];
      }
      throw new Error('Failed to fetch stations');
    }
    return response.json();
  }

  async getStationById(id: number | string): Promise<Station> {
    const token = this.getToken();
    const response = await fetch(`${this.baseUrl}/${id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
    });

    if (!response.ok) {
      if (response.status === 403 || response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
        return {} as Station;
      }
      throw new Error('Failed to fetch station data');
    }
    return response.json();
  }
}
