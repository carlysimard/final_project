from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'
class MusicPageView(TemplateView):
    template_name = 'music.html'
class VideoGamesPageView(TemplateView):
    template_name = 'videoGames.html'
class MoviesAndTvShowsPageView(TemplateView):
    template_name = 'moviesAndTvShows.html'