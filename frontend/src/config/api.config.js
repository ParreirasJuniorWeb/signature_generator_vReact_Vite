/**
 * Configuração da API
 */

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
const API_BASE_PATH = import.meta.env.VITE_API_BASE_PATH || '/api';

export const API_CONFIG = {
  baseURL: `${API_URL}${API_BASE_PATH}`,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
};

export const API_ENDPOINTS = {
  HEALTH: '/health',
  SIGNATURE: '/signature',
  VALIDATE: '/validate',
};

export default API_CONFIG;
