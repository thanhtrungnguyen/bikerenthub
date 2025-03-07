// apps/your-app/src/app/services/authService.ts
import { apiUrl } from '../../environment/apiurl';
import { User } from '../models/user';

export interface LoginResponse {
  pk: number;
  token: string;
}

export class AuthService {

  constructor(private url: string = `${apiUrl}/auth`) { }

  async login(email: string, password: string): Promise<LoginResponse> {
    const response = await fetch(`${this.url}/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }
    return await response.json();
  };

  private getToken(): string | null {
    return localStorage.getItem('token');
  }

  async getUser(): Promise<User> {
    const token = this.getToken();
    if (!token) {
      window.location.href = '/login';
      throw new Error('Not authenticated');
    }
    const response = await fetch(`${this.url}/me/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'accept': '*/*',
        'Authorization': `Bearer ${token}`,
      },
    });
    if (!response.ok) {
      if (response.status === 403 || response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
        return {} as User;
      }
      throw new Error('Failed to fetch user data');
    }
    return response.json();
  }
}
