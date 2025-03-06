import { apiUrl } from "../../environment/apiurl";
import { Station } from "../models/station";

export class StationService {
  constructor(private url: string = `${apiUrl}/stations`) {}

  async getStations(): Promise<Station[]> {
    const response = await fetch(this.url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch bike stations');
    }
    const data = await response.json();
    return data;
  }

  async getStationById(id: string): Promise<Station> {
    const response = await fetch(`${this.url}/${id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch station data');
    }
    const data = await response.json();
    return data;
  }
}
