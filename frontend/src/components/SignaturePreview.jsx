/**
 * Componente de preview da assinatura
 */
import React from 'react';
import Button from './Button';

const SignaturePreview = ({
  signatureUrl,
  isSuccess,
  isLoading,
  onDownload,
}) => {
  return (
    <div className="h-full flex flex-col">
      {/* Título */}
      <div className="mb-6">
        <h2 className="text-2xl md:text-3xl font-bold text-gray-800 text-center">
          {isSuccess ? (
            <span className="flex items-center justify-center text-green-600">
              <svg
                className="w-8 h-8 mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              Assinatura Gerada!
            </span>
          ) : (
            'Preview da Assinatura'
          )}
        </h2>
        <p className="text-center text-gray-600 mt-2">
          {isSuccess
            ? 'Sua assinatura foi gerada com sucesso'
            : 'Preencha o formulário para gerar sua assinatura'}
        </p>
      </div>

      {/* Preview */}
      <div className="flex-1 flex items-center justify-center bg-gray-50 rounded-lg border-2 border-dashed border-gray-300 p-6">
        {isLoading ? (
          <div className="text-center">
            <svg
              className="animate-spin h-16 w-16 text-purple-600 mx-auto mb-4"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              />
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              />
            </svg>
            <p className="text-gray-600 font-medium">Gerando assinatura...</p>
            <p className="text-gray-500 text-sm mt-2">Aguarde um momento</p>
          </div>
        ) : signatureUrl ? (
          <div className="w-full">
            <img
              src={signatureUrl}
              alt="Assinatura gerada"
              className="max-w-full h-auto mx-auto rounded-lg shadow-lg"
            />
          </div>
        ) : (
          <div className="text-center text-gray-400">
            <svg
              className="w-24 h-24 mx-auto mb-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
            <p className="text-lg font-medium">Nenhuma assinatura gerada</p>
            <p className="text-sm mt-2">
              Preencha o formulário e clique em "Gerar Assinatura"
            </p>
          </div>
        )}
      </div>

      {/* Botão de Download */}
      {isSuccess && signatureUrl && (
        <div className="mt-6 space-y-3">
          <Button
            variant="success"
            size="lg"
            onClick={onDownload}
            className="w-full"
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
                  d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                />
              </svg>
            }
          >
            Baixar Assinatura
          </Button>

          {/* Informação sobre uso */}
          <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
            <p className="text-sm text-green-800 flex items-start">
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
                Clique em "Baixar Assinatura" para salvar a imagem no seu computador.
                Depois, você pode configurá-la no seu cliente de e-mail.
              </span>
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default SignaturePreview;
