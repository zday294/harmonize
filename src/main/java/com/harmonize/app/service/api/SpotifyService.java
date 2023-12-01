package com.harmonize.app.service.api;

import java.util.List;

import com.harmonize.app.model.Playlist;
import com.harmonize.app.model.Track;

public interface SpotifyService {
    
    // list playlists for user
    List<Playlist> getUserPlaylists(String userId);
    // list playlist tracks
    List<Track> getPlaylistTracks(String userId, String playlistId);
    // add tracks to playlist
    void addTracksToPlaylist(String userId, String playlistId, List<String> trackUris);
    // search for track
    List<Track> searchTrack(String q);
    // login current user
    void login(String client_id);

}
