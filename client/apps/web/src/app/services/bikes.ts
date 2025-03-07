// apps/your-app/src/app/services/BikeService.ts
import { Bike } from '../models/bike';

export class BikeService {
  private baseUrl: string;

  constructor(baseUrl: string = '/api/bikes') {
    this.baseUrl = baseUrl;
  }

  private getToken(): string | null {
    return localStorage.getItem('token');
  }

  async getBikesForStation(stationId: number): Promise<Bike[]> {
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
      throw new Error('Failed to fetch bikes');
    }
    const allBikes: Bike[] = await response.json();
    return allBikes.filter((bike) => bike.station_id === stationId);
  }
}
