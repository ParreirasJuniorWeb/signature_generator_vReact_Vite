/**
 * Funções de validação de formulário
 */

/**
 * Padrões de validação
 */
export const VALIDATION_PATTERNS = {
  jobTitle: /^.{5,}$/,
  phoneNumber: /^\(\d{2}\)\s\d{4}-\d{4}$/,
  telephoneNumber: /^\(\d{2}\)\s\d{5}-\d{4}$/,
  email: /^[a-zA-Z.]+@saude\.mg\.gov\.br$/,
  department: /^.{5,}$/,
  adress: /^[A-Za-z0-9.,\-\sÀ-úºª°\\/\\]{5,}$/,
};

/**
 * Mensagens de erro
 */
export const ERROR_MESSAGES = {
  fullName: 'Nome completo deve ter no mínimo 5 caracteres (apenas letras)',
  jobTitle: 'Cargo deve ter no mínimo 5 caracteres',
  phoneNumber: 'Telefone deve estar no formato (XX) XXXX-XXXX',
  telephoneNumber: 'Celular deve estar no formato (XX) XXXXX-XXXX',
  email: 'E-mail deve ser do domínio @saude.mg.gov.br',
  department: 'Departamento deve ter no mínimo 5 caracteres',
  adress: 'Endereço deve ter no mínimo 5 caracteres',
  required: 'Este campo é obrigatório',
};

/**
 * Valida um campo individual
 * @param {string} fieldName - Nome do campo
 * @param {string} value - Valor do campo
 * @param {boolean} isRequired - Se o campo é obrigatório
 * @returns {Object} { isValid, error }
 */
export const validateField = (fieldName, value, isRequired = true) => {
  // Verifica se é obrigatório e está vazio
  if (isRequired && (!value || !value.trim())) {
    return {
      isValid: false,
      error: ERROR_MESSAGES.required,
    };
  }

  // Se não é obrigatório e está vazio, é válido
  if (!isRequired && (!value || !value.trim())) {
    return {
      isValid: true,
      error: null,
    };
  }

  // Valida com o padrão específico
  const pattern = VALIDATION_PATTERNS[fieldName];
  if (pattern && !pattern.test(value)) {
    return {
      isValid: false,
      error: ERROR_MESSAGES[fieldName] || 'Formato inválido',
    };
  }

  return {
    isValid: true,
    error: null,
  };
};

/**
 * Valida todos os campos do formulário
 * @param {Object} formData - Dados do formulário
 * @returns {Object} { isValid, errors }
 */
export const validateForm = (formData) => {
  const errors = {};
  let isValid = true;

  // Campos obrigatórios
  const requiredFields = ['fullName', 'jobTitle', 'department', 'phoneNumber', 'email', 'adress'];

  // Valida campos obrigatórios
  requiredFields.forEach((field) => {
    const validation = validateField(field, formData[field], true);
    if (!validation.isValid) {
      errors[field] = validation.error;
      isValid = false;
    }
  });

  // Valida campo opcional (telephoneNumber)
  if (formData.telephoneNumber && formData.telephoneNumber.trim()) {
    const validation = validateField('telephoneNumber', formData.telephoneNumber, false);
    if (!validation.isValid) {
      errors.telephoneNumber = validation.error;
      isValid = false;
    }
  }

  return {
    isValid,
    errors,
  };
};

/**
 * Limpa erros de um campo específico
 * @param {Object} errors - Objeto de erros
 * @param {string} fieldName - Nome do campo
 * @returns {Object} Novo objeto de erros
 */
export const clearFieldError = (errors, fieldName) => {
  const newErrors = { ...errors };
  delete newErrors[fieldName];
  return newErrors;
};
