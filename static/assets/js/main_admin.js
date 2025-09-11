document.addEventListener('DOMContentLoaded', function () {
    // Simple sidebar -> content router
    const links = document.querySelectorAll('.dashboard-sidebar a[data-section]');
    const sections = document.querySelectorAll('.content-section');

    function setActive(sectionId){
        sections.forEach(s => s.classList.toggle('active', s.id === sectionId));
        links.forEach(l => l.classList.toggle('active', l.dataset.section === sectionId));
    }

    links.forEach(link => {
        link.addEventListener('click', e => {
            e.preventDefault();
            const target = link.dataset.section;
            setActive(target);
        });
    });

    // Sidebar logout button handler (red button at bottom)
    const logoutBtnSidebar = document.getElementById('logoutBtnSidebar');
    if (logoutBtnSidebar) logoutBtnSidebar.addEventListener('click', ()=>{
        setActive('logout');
    });

    // Sidebar open/close (hamburger) for small screens
    const sidebarToggle = document.getElementById('sidebarToggle');
    const dashboardSidebar = document.getElementById('dashboardSidebar');
    if(sidebarToggle && dashboardSidebar){
        sidebarToggle.addEventListener('click', ()=>{
            dashboardSidebar.classList.toggle('open');
        });

        // close sidebar when clicking a link (better UX on mobile)
        document.querySelectorAll('.dashboard-sidebar a[data-section]').forEach(a=>{
            a.addEventListener('click', ()=> dashboardSidebar.classList.remove('open'));
        });

        // close when clicking outside the sidebar
        document.addEventListener('click', function(e){
            if(dashboardSidebar.classList.contains('open')){
                const path = e.composedPath ? e.composedPath() : (e.path || []);
                const withinSidebar = path.includes(dashboardSidebar) || path.includes(sidebarToggle);
                if(!withinSidebar) dashboardSidebar.classList.remove('open');
            }
        });
    }

    // Optional: logout confirmation inside logout section
    // const logoutBtn = document.getElementById('logoutBtn');
    // if(logoutBtn) logoutBtn.addEventListener('click', ()=> alert('Siz tizimdan chiqdingiz (demo).'));



    // Add click handler for any file links to allow backend download logging if needed
    document.querySelectorAll('.file-link').forEach(a=>{
        a.addEventListener('click', function(e){
            // Example: hit backend to register the download (replace URL with real endpoint)
            // navigator.sendBeacon('/api/log-download', JSON.stringify({file: this.href}));
            // For demo nothing else is done; link will open in new tab
        });
    });

    // Image preview helpers for the form file inputs
    function setupImagePreview(fileInputId, previewContainerId){
        const input = document.getElementById(fileInputId);
        const preview = document.getElementById(previewContainerId);
        if(!input || !preview) return;

        input.addEventListener('change', function(){
            const file = this.files && this.files[0];
            preview.innerHTML = '';
            if(!file) return;
            const img = document.createElement('img');
            img.alt = 'Preview';
            img.style.maxWidth = '100%';
            img.style.height = 'auto';
            preview.appendChild(img);

            const reader = new FileReader();
            reader.onload = function(e){ img.src = e.target.result; };
            reader.readAsDataURL(file);
        });
    }

    // Initialize previews (ids used in templates)
    setupImagePreview('yangilikImage', 'yangilikPreview');
    setupImagePreview('tanlovImage', 'tanlovPreview');

});
