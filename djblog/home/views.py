from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Datos dinámicos para el hero
        context['hero_title'] = 'Soluciones Digitales Innovadoras'
        context['hero_subtitle'] = 'Transformamos tus ideas en realidad con tecnología de vanguardia'

        # Datos dinámicos para servicios
        context['services'] = [
            {'icon': 'fa-globe', 'title': 'Desarrollo Web',
             'description': 'Sitios web modernos con Django, React y Bootstrap'},
            {'icon': 'fa-mobile-alt', 'title': 'Apps Móviles',
             'description': 'Aplicaciones nativas e híbridas para iOS y Android'},
            {'icon': 'fa-brain', 'title': 'Inteligencia Artificial',
             'description': 'Soluciones con IA y Machine Learning'},
            {'icon': 'fa-chart-line', 'title': 'Consultoría TI',
             'description': 'Asesoramiento tecnológico para tu empresa'},
            {'icon': 'fa-cloud-upload-alt', 'title': 'Cloud Computing',
             'description': 'Infraestructura en AWS, Azure y Google Cloud'},
            {'icon': 'fa-shield-alt', 'title': 'Ciberseguridad', 'description': 'Protección avanzada para tu negocio'},
        ]

        # Datos dinámicos para contadores
        context['counters'] = [
            {'icon': 'fa-project-diagram', 'value': 150, 'label': 'Proyectos'},
            {'icon': 'fa-users', 'value': 100, 'label': 'Clientes'},
            {'icon': 'fa-trophy', 'value': 25, 'label': 'Premios'},
        ]

        # Datos dinámicos para testimonios
        context['testimonials'] = [
            {'name': 'Juan Pérez', 'position': 'CEO Empresa X',
             'text': 'Excelente servicio, superaron nuestras expectativas.', 'rating': 5,
             'image': 'https://randomuser.me/api/portraits/men/1.jpg'},
            {'name': 'María González', 'position': 'CTO Startup Y',
             'text': 'La mejor decisión que tomamos. Nuestra app móvil es increíble.', 'rating': 5,
             'image': 'https://randomuser.me/api/portraits/women/1.jpg'},
            {'name': 'Carlos López', 'position': 'Director Tech Z',
             'text': 'Profesionales altamente capacitados. La consultoría en IA transformó nuestro negocio.',
             'rating': 5, 'image': 'https://randomuser.me/api/portraits/men/2.jpg'},
        ]

        # Datos dinámicos para blog
        context['blog_posts'] = [
            {'title': 'Tendencias en IA 2025', 'date': '15 Jun 2026',
             'summary': 'Descubre las últimas tendencias en inteligencia artificial.',
             'image': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400'},
            {'title': 'Desarrollo Web Moderno', 'date': '10 Jun 2026',
             'summary': 'Las mejores prácticas y frameworks para desarrollo web.',
             'image': 'https://images.unsplash.com/photo-1461749280685-d4ba630d1eca?w=400'},
            {'title': 'Ciberseguridad Empresarial', 'date': '5 Jun 2026',
             'summary': 'Consejos para proteger tu negocio de amenazas cibernéticas.',
             'image': 'https://images.unsplash.com/photo-1556075798-4825dfaaf498?w=400'},
        ]

        return context
