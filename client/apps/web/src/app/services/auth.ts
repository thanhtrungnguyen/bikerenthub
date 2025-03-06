// apps/your-app/src/app/services/authService.ts
import { apiUrl } from '../../environment/apiurl';
import { User } from '../models/user';

export class AuthService {

  constructor(private url: string = `${apiUrl}/auth`) {}

  async login(email: string, password: string): Promise<string> {
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

  async getCurrentUser(jwt: string): Promise<User> {
    const response = await fetch(`${this.url}/me/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'accept': '*/*',
        'Authorization': `Bearer ${jwt}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch user data');
    }

    // Assuming the backend returns the user data directly as JSON
    const data = await response.json();
    return data;
  }
}
