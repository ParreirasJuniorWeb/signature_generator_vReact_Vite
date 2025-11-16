/**
 * Componente do formulário de assinatura
 */
import React from 'react';
import InputField from './InputField';
import Button from './Button';
import { formatPhone, formatTelephone } from '../utils/formatters';

const SignatureForm = ({
  formData,
  errors,
  isLoading,
  onFieldChange,
  onFieldBlur,
  onSubmit,
  onReset,
}) => {
  /**
   * Manipula mudança de campo com formatação
   */
  const handleFieldChange = (e) => {
    const { name, value } = e.target;
    let formattedValue = value;

    // Aplica formatação específica
    switch (name) {
      case 'phoneNumber':
        formattedValue = formatPhone(value);
        break;
      case 'telephoneNumber':
        formattedValue = formatTelephone(value);
        break;
      default:
        formattedValue = value;
    }

    onFieldChange(name, formattedValue);
  };

  /**
   * Manipula blur do campo
   */
  const handleFieldBlur = (e) => {
    const { name, value } = e.target;
    onFieldBlur(name, value);
  };

  /**
   * Manipula submit do formulário
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {/* Nome Completo */}
      <InputField
        label="Nome Completo"
        name="fullName"
        value={formData.fullName}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.fullName}
        placeholder="Ex: João Pedro Silva"
        required
        maxLength={100}
        disabled={isLoading}
      />

      {/* Cargo */}
      <InputField
        label="Cargo"
        name="jobTitle"
        value={formData.jobTitle}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.jobTitle}
        placeholder="Ex: Coordenador de Saúde Pública"
        required
        maxLength={100}
        disabled={isLoading}
      />

      {/* Departamento */}
      <InputField
        label="Departamento"
        name="department"
        value={formData.department}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.department}
        placeholder="Ex: COORDENADORIA DE VIGILÂNCIA EPIDEMIOLÓGICA"
        required
        maxLength={150}
        disabled={isLoading}
      />

      {/* Telefone */}
      <InputField
        label="Telefone"
        name="phoneNumber"
        type="tel"
        value={formData.phoneNumber}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.phoneNumber}
        placeholder="(31) 3916-0000"
        required
        maxLength={15}
        disabled={isLoading}
      />

      {/* Celular (Opcional) */}
      <InputField
        label="Celular"
        name="telephoneNumber"
        type="tel"
        value={formData.telephoneNumber}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.telephoneNumber}
        placeholder="(31) 98765-4321"
        maxLength={16}
        disabled={isLoading}
      />

      {/* E-mail */}
      <InputField
        label="E-mail"
        name="email"
        type="email"
        value={formData.email}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.email}
        placeholder="nome.sobrenome@saude.mg.gov.br"
        required
        maxLength={100}
        disabled={isLoading}
      />

      {/* Endereço */}
      <InputField
        label="Endereço"
        name="adress"
        value={formData.adress}
        onChange={handleFieldChange}
        onBlur={handleFieldBlur}
        error={errors.adress}
        placeholder="Cidade Administrativa, Prédio Minas, 1º andar"
        required
        maxLength={200}
        disabled={isLoading}
      />

      {/* Botões */}
      <div className="flex gap-3 pt-4">
        <Button
          type="submit"
          variant="primary"
          size="lg"
          loading={isLoading}
          disabled={isLoading}
          className="flex-1"
          icon={
            <svg
              className="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
              />
            </svg>
          }
        >
          Gerar Assinatura
        </Button>

        <Button
          type="button"
          variant="outline"
          size="lg"
          onClick={onReset}
          disabled={isLoading}
          icon={
            <svg
              className="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
              />
            </svg>
          }
        >
          Limpar
        </Button>
      </div>

      {/* Informação */}
      <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
        <p className="text-sm text-blue-800 flex items-start">
          <svg
            className="w-5 h-5 mr-2 flex-shrink-0 mt-0.5"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path
              fillRule="evenodd"
              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
              clipRule="evenodd"
            />
          </svg>
          <span>
            Preencha todos os campos obrigatórios (*) para gerar sua assinatura.
            O celular é opcional.
          </span>
        </p>
      </div>
    </form>
  );
};

export default SignatureForm;
