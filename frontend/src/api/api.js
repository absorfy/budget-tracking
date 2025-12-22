const API_URL = import.meta.env.VITE_API_URL || '/api';

async function request(path, options = {}) {
    const res = await fetch(`${API_URL}${path}`, {
        headers: { 'Content-Type': 'application/json' },
        ...options,
    });
    if (!res.ok) {
        const text = await res.text();
        throw new Error(text || res.statusText);
    }
    const contentType = res.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
        return null;
    }
    const text = await res.text();
    return text ? JSON.parse(text) : null;
}

export const api = {
    getWallets: () => request('/wallets/'),
    getWallet: (id) => request(`/wallets/${id}/`),
    createWallet: (data) => request('/wallets/', { method: 'POST', body: JSON.stringify(data) }),
    getTransactions: (walletId) => request(`/transactions/?wallet=${walletId}`),
    createTransaction: (data) =>
        request('/transactions/', { method: 'POST', body: JSON.stringify(data) }),
    deleteTransaction: (id) => request(`/transactions/${id}/`, { method: 'DELETE' }),
};
