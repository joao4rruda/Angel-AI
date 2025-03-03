from supabase import create_client, Client

# Configurações do Supabase
SUPABASE_URL = "https://hferfjctasmpesfnccwb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhmZXJmamN0YXNtcGVzZm5jY3diIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAzMTQ4MjUsImV4cCI6MjA1NTg5MDgyNX0.PQJUIhFoNhXj-oTy8YM6VCqPskW9jG6gZOLVzhJUH0w"

# Criando o cliente Supabase uma única vez
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_client() -> Client:
    """Retorna o cliente Supabase já instanciado."""
    return supabase
