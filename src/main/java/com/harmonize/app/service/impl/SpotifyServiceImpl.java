package com.harmonize.app.service.impl;

import java.util.List;

import org.springframework.stereotype.Service;

import com.harmonize.app.model.Playlist;
import com.harmonize.app.model.Track;
import com.harmonize.app.service.api.SpotifyService;

@Service
public class SpotifyServiceImpl implements SpotifyService{

    @Override
    public List<Playlist> getUserPlaylists(String userId) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getUserPlaylists'");
    }

    @Override
    public List<Track> getPlaylistTracks(String userId, String playlistId) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getPlaylistTracks'");
    }

    @Override
    public void addTracksToPlaylist(String userId, String playlistId, List<String> trackUris) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'addTracksToPlaylist'");
    }

    @Override
    public List<Track> searchTrack(String q) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'searchTracks'");
    }

    @Override
    public void login(String client_id) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'login'");
    }
    
}
