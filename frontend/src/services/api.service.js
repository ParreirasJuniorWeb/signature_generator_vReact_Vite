/**
 * Serviço de comunicação com a API
 * Gerencia todas as requisições HTTP
 */
import axios from 'axios';
import { API_CONFIG, API_ENDPOINTS } from '../config/api.config';

// Cria instância do axios com configurações base
const apiClient = axios.create(API_CONFIG);

// Interceptor de requisição
apiClient.interceptors.request.use(
  (config) => {
    // Adiciona timestamp para evitar cache
    config.params = {
      ...config.params,
      _t: Date.now(),
    };
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor de resposta
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Tratamento de erros global
    if (error.response) {
      // Erro da API
      const { status, data } = error.response;
      console.error(`API Error ${status}:`, data);
      
      // Customiza mensagem de erro
      error.message = data.error || data.message || 'Erro ao comunicar com o servidor';
      error.errors = data.errors || {};
    } else if (error.request) {
      // Erro de rede
      console.error('Network Error:', error.request);
      error.message = 'Erro de conexão. Verifique sua internet e tente novamente.';
    } else {
      // Erro desconhecido
      console.error('Error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

/**
 * Serviço de API
 */
const ApiService = {
  /**
   * Verifica o status da API
   * @returns {Promise<Object>} Status da API
   */
  async healthCheck() {
    try {
      const response = await apiClient.get(API_ENDPOINTS.HEALTH);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Valida os dados do formulário
   * @param {Object} userData - Dados do usuário
   * @returns {Promise<Object>} Dados validados
   */
  async validateData(userData) {
    try {
      const response = await apiClient.post(API_ENDPOINTS.VALIDATE, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Gera a assinatura
   * @param {Object} userData - Dados do usuário
   * @returns {Promise<Blob>} Imagem da assinatura
   */
  async generateSignature(userData) {
    try {
      const response = await apiClient.post(API_ENDPOINTS.SIGNATURE, userData, {
        responseType: 'blob',
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default ApiService;
