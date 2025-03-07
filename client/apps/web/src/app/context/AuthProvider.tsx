import React, { createContext, useState, ReactNode } from 'react';

export interface AuthContextType {
  auth: {
    user: unknown; // Adjust this type as needed
    accessToken: string;
  };
  setAuth: React.Dispatch<
    React.SetStateAction<{
      user: unknown;
      accessToken: string;
    }>
  >;
}

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [auth, setAuth] = useState<{ user: unknown; accessToken: string }>({
    user: null,
    accessToken: '',
  });

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
