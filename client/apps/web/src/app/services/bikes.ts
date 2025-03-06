// apps/your-app/src/app/services/BikeService.ts
import { Bike } from '../models/bike';

export class BikeService {
  private baseUrl: string;

  constructor(baseUrl: string = '/api/bikes') {
    this.baseUrl = baseUrl;
  }

  async getBikesForStation(stationId: number): Promise<Bike[]> {
    const response = await fetch(this.baseUrl, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
    });

    if (!response.ok) {
      if (response.status === 403) {
        window.location.href = '/login';
        return [];
      }
      throw new Error('Failed to fetch bikes');
    }
    const allBikes: Bike[] = await response.json();
    return allBikes.filter((bike) => bike.station_id === stationId);
  }
}
