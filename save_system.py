"""Game state persistence — save and load game progress."""

import json
import os
from pathlib import Path
from datetime import datetime

SAVES_DIR = Path(__file__).resolve().parent / "saves"


def ensure_saves_dir():
    """Create saves directory if it doesn't exist."""
    SAVES_DIR.mkdir(exist_ok=True)


def save_game(game_obj, filename=None):
    """
    Save game state to file.
    
    Args:
        game_obj: Game instance with player, enemies, gold, level, etc.
        filename: Custom save filename (default: auto-generated with timestamp)
    
    Returns:
        Path to saved file or None on error
    """
    ensure_saves_dir()
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"save_{timestamp}.json"
    
    filepath = SAVES_DIR / filename
    
    try:
        # Serialize game state
        save_data = {
            "timestamp": datetime.now().isoformat(),
            "player": {
                "name": game_obj.player.name,
                "health": game_obj.player.health,
                "max_health": game_obj.player.max_health,
                "attack_power": game_obj.player.attack_power,
                "defense": game_obj.player.defense,
                "gold": game_obj.player.gold,
                "experience": game_obj.player.experience,
                "level": game_obj.player.level,
                "inventory": game_obj.player.inventory if hasattr(game_obj.player, 'inventory') else []
            },
            "game_state": {
                "current_room": str(game_obj.game_map),
                "explored_paths": game_obj.explored_paths if hasattr(game_obj, 'explored_paths') else []
            }
        }
        
        with open(filepath, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        print(f"✓ Game saved to: {filepath}")
        return filepath
    
    except Exception as e:
        print(f"✗ Error saving game: {e}")
        return None


def load_game(filename):
    """
    Load game state from file.
    
    Args:
        filename: Save file name (e.g., 'save_20260819_123456.json')
    
    Returns:
        Loaded save data or None on error
    """
    ensure_saves_dir()
    filepath = SAVES_DIR / filename
    
    try:
        if not filepath.exists():
            print(f"✗ Save file not found: {filename}")
            return None
        
        with open(filepath, 'r') as f:
            save_data = json.load(f)
        
        print(f"✓ Game loaded from: {filepath}")
        print(f"  Saved at: {save_data.get('timestamp', 'unknown')}")
        print(f"  Player: {save_data['player']['name']} | Level {save_data['player']['level']} | HP: {save_data['player']['health']}/{save_data['player']['max_health']}")
        
        return save_data
    
    except Exception as e:
        print(f"✗ Error loading game: {e}")
        return None


def list_saves():
    """List all available save files."""
    ensure_saves_dir()
    
    saves = sorted(SAVES_DIR.glob("save_*.json"), reverse=True)
    
    if not saves:
        print("No save files found.")
        return []
    
    print(f"\n{'Slot':<3} | {'Timestamp':<19} | {'File':<40}")
    print("-" * 70)
    
    results = []
    for i, save_file in enumerate(saves, 1):
        try:
            with open(save_file, 'r') as f:
                data = json.load(f)
            timestamp = data.get('timestamp', 'unknown')[:19]
            player_name = data['player']['name']
            level = data['player']['level']
            print(f"{i:<3} | {timestamp} | {player_name} - Level {level} - {save_file.name}")
            results.append(save_file.name)
        except Exception as e:
            print(f"{i:<3} | ERROR | {save_file.name}")
    
    return results


def delete_save(filename):
    """Delete a save file."""
    ensure_saves_dir()
    filepath = SAVES_DIR / filename
    
    try:
        if filepath.exists():
            filepath.unlink()
            print(f"✓ Save deleted: {filename}")
            return True
        else:
            print(f"✗ Save file not found: {filename}")
            return False
    except Exception as e:
        print(f"✗ Error deleting save: {e}")
        return False


def restore_player_state(game_obj, save_data):
    """
    Apply loaded save data to game object.
    
    Args:
        game_obj: Game instance
        save_data: Loaded save data from load_game()
    """
    try:
        player_data = save_data['player']
        game_obj.player.name = player_data['name']
        game_obj.player.health = player_data['health']
        game_obj.player.max_health = player_data['max_health']
        game_obj.player.attack_power = player_data['attack_power']
        game_obj.player.defense = player_data['defense']
        game_obj.player.gold = player_data['gold']
        game_obj.player.experience = player_data['experience']
        game_obj.player.level = player_data['level']
        
        if 'inventory' in player_data and hasattr(game_obj.player, 'inventory'):
            game_obj.player.inventory = player_data['inventory']
        
        print("✓ Player state restored successfully")
        return True
    except Exception as e:
        print(f"✗ Error restoring player state: {e}")
        return False
