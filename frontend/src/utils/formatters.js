/**
 * Funções de formatação de dados
 */

/**
 * Formata número de telefone fixo
 * @param {string} value - Valor a ser formatado
 * @returns {string} Telefone formatado
 */
export const formatPhone = (value) => {
  // Remove tudo que não é dígito
  const cleaned = value.replace(/\D/g, '');
  
  // Limita a 10 dígitos
  const limited = cleaned.substring(0, 10);
  
  // Aplica a máscara (XX) XXXX-XXXX
  if (limited.length <= 2) {
    return limited;
  } else if (limited.length <= 6) {
    return `(${limited.slice(0, 2)}) ${limited.slice(2)}`;
  } else {
    return `(${limited.slice(0, 2)}) ${limited.slice(2, 6)}-${limited.slice(6)}`;
  }
};

/**
 * Formata número de celular
 * @param {string} value - Valor a ser formatado
 * @returns {string} Celular formatado
 */
export const formatTelephone = (value) => {
  // Remove tudo que não é dígito
  const cleaned = value.replace(/\D/g, '');
  
  // Limita a 11 dígitos
  const limited = cleaned.substring(0, 11);
  
  // Aplica a máscara (XX) XXXXX-XXXX
  if (limited.length <= 2) {
    return limited;
  } else if (limited.length <= 7) {
    return `(${limited.slice(0, 2)}) ${limited.slice(2)}`;
  } else {
    return `(${limited.slice(0, 2)}) ${limited.slice(2, 7)}-${limited.slice(7)}`;
  }
};

/**
 * Formata nome (capitaliza corretamente)
 * @param {string} value - Nome a ser formatado
 * @returns {string} Nome formatado
 */
export const formatName = (value) => {
  const articles = ['de', 'da', 'das', 'do', 'dos', 'e', 'em'];
  
  return value
    .toLowerCase()
    .split(' ')
    .map((word) => {
      if (articles.includes(word)) {
        return word;
      }
      return word.charAt(0).toUpperCase() + word.slice(1);
    })
    .join(' ');
};

/**
 * Formata departamento (maiúsculas)
 * @param {string} value - Departamento a ser formatado
 * @returns {string} Departamento formatado
 */
export const formatDepartment = (value) => {
  return value.toUpperCase();
};

/**
 * Formata endereço
 * @param {string} value - Endereço a ser formatado
 * @returns {string} Endereço formatado
 */
export const formatAddress = (value) => {
  const acronyms = ['BH', 'MG', 'SRS', 'GRS'];
  
  let formatted = formatName(value);
  
  // Substitui siglas conhecidas por maiúsculas
  acronyms.forEach((acronym) => {
    const regex = new RegExp(`\\b${acronym}\\b`, 'gi');
    formatted = formatted.replace(regex, acronym);
  });
  
  return formatted;
};

/**
 * Remove formatação de telefone
 * @param {string} value - Telefone formatado
 * @returns {string} Apenas dígitos
 */
export const unformatPhone = (value) => {
  return value.replace(/\D/g, '');
};

/**
 * Cria URL de download para blob
 * @param {Blob} blob - Blob da imagem
 * @param {string} filename - Nome do arquivo
 */
export const downloadBlob = (blob, filename = 'assinatura.png') => {
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  window.URL.revokeObjectURL(url);
};

/**
 * Converte blob em URL para preview
 * @param {Blob} blob - Blob da imagem
 * @returns {string} URL da imagem
 */
export const blobToUrl = (blob) => {
  return window.URL.createObjectURL(blob);
};
