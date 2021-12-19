from django.urls import path
from .views import HomePageView, MusicPageView, VideoGamesPageView, MoviesAndTvShowsPageView

urlpatterns = [
    path('moviesAndTvShows/', MoviesAndTvShowsPageView.as_view(), name='moviesAndTvShows'),
    path('videoGames/', VideoGamesPageView.as_view(), name='videoGames'),
    path('music/', MusicPageView.as_view(), name='music'),
    path('', HomePageView.as_view(), name='home'),
]