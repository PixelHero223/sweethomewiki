function copyIP(text, btnElement) {
    navigator.clipboard.writeText(text);

    const originalText = btnElement.innerText;
    btnElement.innerText = 'Copied!';
    btnElement.style.color = '#00d26a';

    setTimeout(() => {
        btnElement.innerText = originalText;
        btnElement.style.color = '';
    }, 2000);
}