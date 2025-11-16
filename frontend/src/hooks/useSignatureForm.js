/**
 * Custom Hook para gerenciar o formulário de assinatura
 */
import { useState, useCallback } from 'react';
import ApiService from '../services/api.service';
import { validateForm, validateField, clearFieldError } from '../utils/validators';
import { downloadBlob, blobToUrl } from '../utils/formatters';

/**
 * Hook para gerenciar o formulário de assinatura
 */
export const useSignatureForm = () => {
  // Estado do formulário
  const [formData, setFormData] = useState({
    fullName: '',
    jobTitle: '',
    department: '',
    phoneNumber: '',
    telephoneNumber: '',
    email: '',
    adress: '',
  });

  // Estado de erros
  const [errors, setErrors] = useState({});

  // Estado de loading
  const [isLoading, setIsLoading] = useState(false);

  // Estado da assinatura gerada
  const [signatureUrl, setSignatureUrl] = useState(null);
  const [signatureBlob, setSignatureBlob] = useState(null);

  // Estado de sucesso
  const [isSuccess, setIsSuccess] = useState(false);

  /**
   * Atualiza um campo do formulário
   */
  const updateField = useCallback((fieldName, value) => {
    setFormData((prev) => ({
      ...prev,
      [fieldName]: value,
    }));

    // Limpa erro do campo ao digitar
    if (errors[fieldName]) {
      setErrors((prev) => clearFieldError(prev, fieldName));
    }
  }, [errors]);

  /**
   * Valida um campo específico
   */
  const validateSingleField = useCallback((fieldName, value) => {
    const isRequired = fieldName !== 'telephoneNumber';
    const validation = validateField(fieldName, value, isRequired);
    
    if (!validation.isValid) {
      setErrors((prev) => ({
        ...prev,
        [fieldName]: validation.error,
      }));
    } else {
      setErrors((prev) => clearFieldError(prev, fieldName));
    }
    
    return validation.isValid;
  }, []);

  /**
   * Reseta o formulário
   */
  const resetForm = useCallback(() => {
    setFormData({
      fullName: '',
      jobTitle: '',
      department: '',
      phoneNumber: '',
      telephoneNumber: '',
      email: '',
      adress: '',
    });
    setErrors({});
    setSignatureUrl(null);
    setSignatureBlob(null);
    setIsSuccess(false);
  }, []);

  /**
   * Gera a assinatura
   */
  const generateSignature = useCallback(async () => {
    try {
      // Valida o formulário
      const validation = validateForm(formData);
      
      if (!validation.isValid) {
        setErrors(validation.errors);
        return {
          success: false,
          error: 'Por favor, corrija os erros no formulário',
        };
      }

      setIsLoading(true);
      setErrors({});

      // Chama a API
      const blob = await ApiService.generateSignature(formData);

      // Cria URL para preview
      const url = blobToUrl(blob);
      
      setSignatureBlob(blob);
      setSignatureUrl(url);
      setIsSuccess(true);

      return {
        success: true,
        blob,
        url,
      };
    } catch (error) {
      console.error('Erro ao gerar assinatura:', error);
      
      // Trata erros de validação da API
      if (error.errors) {
        setErrors(error.errors);
      }

      return {
        success: false,
        error: error.message || 'Erro ao gerar assinatura',
      };
    } finally {
      setIsLoading(false);
    }
  }, [formData]);

  /**
   * Faz download da assinatura
   */
  const downloadSignature = useCallback(() => {
    if (signatureBlob) {
      const filename = `assinatura_${formData.fullName.replace(/\s+/g, '_').toLowerCase()}.png`;
      downloadBlob(signatureBlob, filename);
      return true;
    }
    return false;
  }, [signatureBlob, formData.fullName]);

  /**
   * Valida dados sem gerar assinatura
   */
  const validateOnly = useCallback(async () => {
    try {
      // Valida localmente primeiro
      const validation = validateForm(formData);
      
      if (!validation.isValid) {
        setErrors(validation.errors);
        return {
          success: false,
          errors: validation.errors,
        };
      }

      setIsLoading(true);
      setErrors({});

      // Valida na API
      await ApiService.validateData(formData);

      return {
        success: true,
      };
    } catch (error) {
      console.error('Erro ao validar dados:', error);
      
      if (error.errors) {
        setErrors(error.errors);
      }

      return {
        success: false,
        error: error.message || 'Erro ao validar dados',
        errors: error.errors || {},
      };
    } finally {
      setIsLoading(false);
    }
  }, [formData]);

  return {
    // Estado
    formData,
    errors,
    isLoading,
    signatureUrl,
    signatureBlob,
    isSuccess,
    
    // Ações
    updateField,
    validateSingleField,
    resetForm,
    generateSignature,
    downloadSignature,
    validateOnly,
  };
};

export default useSignatureForm;
