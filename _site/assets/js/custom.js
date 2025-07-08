// Custom JavaScript for enhanced blog experience

document.addEventListener('DOMContentLoaded', function() {
  // Reading progress indicator
  function createReadingProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    progressBar.innerHTML = '<div class="progress-bar"></div>';
    document.body.appendChild(progressBar);
    
    const progressBarFill = progressBar.querySelector('.progress-bar');
    
    window.addEventListener('scroll', () => {
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight - windowHeight;
      const scrolled = window.scrollY;
      const progress = (scrolled / documentHeight) * 100;
      progressBarFill.style.width = progress + '%';
    });
  }
  
  // Back to top button
  function createBackToTop() {
    const button = document.createElement('div');
    button.className = 'back-to-top';
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" /></svg>';
    document.body.appendChild(button);
    
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        button.classList.add('visible');
      } else {
        button.classList.remove('visible');
      }
    });
    
    button.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
  
  // Enhanced image loading with fade-in effect
  function enhanceImages() {
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
      img.style.opacity = '0';
      img.style.transition = 'opacity 0.3s ease';
      
      if (img.complete) {
        img.style.opacity = '1';
      } else {
        img.addEventListener('load', () => {
          img.style.opacity = '1';
        });
      }
    });
  }
  
  // Add copy code functionality enhancement
  function enhanceCodeBlocks() {
    const codeBlocks = document.querySelectorAll('pre');
    
    codeBlocks.forEach(block => {
      block.style.position = 'relative';
      
      // Add hover effect
      block.addEventListener('mouseenter', () => {
        block.style.transform = 'translateY(-2px)';
        block.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.1)';
      });
      
      block.addEventListener('mouseleave', () => {
        block.style.transform = 'translateY(0)';
        block.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
      });
    });
  }
  
  // Social sharing buttons
  function createSocialShare() {
    const article = document.querySelector('article.content');
    if (!article) return;
    
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    
    const shareContainer = document.createElement('div');
    shareContainer.className = 'social-share';
    shareContainer.innerHTML = `
      <a href="https://twitter.com/intent/tweet?url=${url}&text=${title}" target="_blank" rel="noopener" class="twitter" title="Share on Twitter">
        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
      </a>
      <a href="https://www.linkedin.com/sharing/share-offsite/?url=${url}" target="_blank" rel="noopener" class="linkedin" title="Share on LinkedIn">
        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      </a>
      <a href="mailto:?subject=${title}&body=${url}" class="email" title="Share via Email">
        <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
      </a>
    `;
    
    // Insert after the article content
    const articleContent = article.querySelector('.content');
    if (articleContent) {
      articleContent.appendChild(shareContainer);
    }
  }
  
  // Initialize all enhancements
  if (document.querySelector('article')) {
    createReadingProgress();
    createBackToTop();
    createSocialShare();
  }
  
  enhanceImages();
  enhanceCodeBlocks();
  
  // Theme transition enhancement
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
        // Smooth transition when theme changes
        document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
      }
    });
  });
  
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ['class']
  });
});