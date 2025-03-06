// apps/your-app/src/app/services/authService.ts
import { apiUrl } from '../../environment/apiurl';
import { User } from '../models/user';

export interface LoginResponse {
  pk: number;
  token: string;
}

export class AuthService {

  constructor(private url: string = `${apiUrl}/auth`) {}

  async login(email: string, password: string): Promise<LoginResponse> {
    const response = await fetch(`${this.url}/jwt/login/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const data = await response.json();
    const jwt = data.token;
    return jwt;
  };

  async getCurrentUser(): Promise<User> {
    const response = await fetch(`${this.url}/me/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        accept: '*/*',
      },
      credentials: 'include',
    });
    if (!response.ok) {
      if (response.status === 403) {
        window.location.href = '/login';
        return {} as User;
      }
      throw new Error('Failed to fetch user data');
    }
    return response.json();
  }
}
