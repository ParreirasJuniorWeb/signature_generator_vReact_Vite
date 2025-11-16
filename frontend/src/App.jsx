/**
 * Componente principal da aplicação
 */
import React, { useState } from 'react';
import SignatureForm from './components/SignatureForm';
import SignaturePreview from './components/SignaturePreview';
import { useSignatureForm } from './hooks/useSignatureForm';

function App() {
  const [showAlert, setShowAlert] = useState(null);

  const {
    formData,
    errors,
    isLoading,
    signatureUrl,
    isSuccess,
    updateField,
    validateSingleField,
    resetForm,
    generateSignature,
    downloadSignature,
  } = useSignatureForm();

  /**
   * Manipula geração de assinatura
   */
  const handleGenerate = async () => {
    const result = await generateSignature();
    
    if (result.success) {
      setShowAlert({
        type: 'success',
        message: 'Assinatura gerada com sucesso!',
      });
      
      // Remove alerta após 5 segundos
      setTimeout(() => setShowAlert(null), 5000);
    } else {
      setShowAlert({
        type: 'error',
        message: result.error || 'Erro ao gerar assinatura',
      });
      
      // Remove alerta após 7 segundos
      setTimeout(() => setShowAlert(null), 7000);
    }
  };

  /**
   * Manipula download
   */
  const handleDownload = () => {
    const success = downloadSignature();
    
    if (success) {
      setShowAlert({
        type: 'success',
        message: 'Assinatura baixada com sucesso!',
      });
      
      setTimeout(() => setShowAlert(null), 3000);
    }
  };

  /**
   * Manipula reset do formulário
   */
  const handleReset = () => {
    if (window.confirm('Tem certeza que deseja limpar o formulário?')) {
      resetForm();
      setShowAlert(null);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-orange-50">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center">
                <svg
                  className="w-8 h-8 text-white"
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
              </div>
              <div>
                <h1 className="text-2xl md:text-3xl font-bold text-gray-800">
                  Gerador de Assinaturas
                </h1>
                <p className="text-sm text-gray-600">
                  Secretaria de Estado de Saúde de Minas Gerais
                </p>
              </div>
            </div>
            
            {/* Badge de versão */}
            <div className="hidden md:block">
              <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-sm font-medium">
                v2.0.0
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* Alert */}
      {showAlert && (
        <div className="container mx-auto px-4 mt-4">
          <div
            className={`
              p-4 rounded-lg flex items-center justify-between
              ${showAlert.type === 'success' ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}
            `}
          >
            <div className="flex items-center">
              {showAlert.type === 'success' ? (
                <svg
                  className="w-6 h-6 text-green-600 mr-3"
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
              ) : (
                <svg
                  className="w-6 h-6 text-red-600 mr-3"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              )}
              <p
                className={`font-medium ${showAlert.type === 'success' ? 'text-green-800' : 'text-red-800'}`}
              >
                {showAlert.message}
              </p>
            </div>
            <button
              onClick={() => setShowAlert(null)}
              className="text-gray-500 hover:text-gray-700"
            >
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
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Formulário */}
          <div className="bg-white rounded-xl shadow-lg p-6 md:p-8">
            <div className="mb-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-2">
                Dados da Assinatura
              </h2>
              <p className="text-gray-600">
                Preencha seus dados para gerar a assinatura personalizada
              </p>
            </div>
            
            <SignatureForm
              formData={formData}
              errors={errors}
              isLoading={isLoading}
              onFieldChange={updateField}
              onFieldBlur={validateSingleField}
              onSubmit={handleGenerate}
              onReset={handleReset}
            />
          </div>

          {/* Preview */}
          <div className="bg-white rounded-xl shadow-lg p-6 md:p-8">
            <SignaturePreview
              signatureUrl={signatureUrl}
              isSuccess={isSuccess}
              isLoading={isLoading}
              onDownload={handleDownload}
            />
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="container mx-auto px-4 py-6">
          <div className="flex flex-col md:flex-row items-center justify-between">
            <p className="text-gray-600 text-sm text-center md:text-left mb-2 md:mb-0">
              © 2025 Secretaria de Estado de Saúde de Minas Gerais
            </p>
            <div className="flex items-center space-x-4">
              <a
                href="#"
                className="text-gray-600 hover:text-purple-600 text-sm transition-colors"
              >
                Ajuda
              </a>
              <span className="text-gray-400">•</span>
              <a
                href="#"
                className="text-gray-600 hover:text-purple-600 text-sm transition-colors"
              >
                Suporte
              </a>
              <span className="text-gray-400">•</span>
              <a
                href="#"
                className="text-gray-600 hover:text-purple-600 text-sm transition-colors"
              >
                Documentação
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
