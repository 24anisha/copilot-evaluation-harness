package dab.server.network;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.net.SocketException;

import dab.common.entity.Enemy;
import dab.common.entity.Player;

public class ClientConnection
{
	private Socket socket;
	private ObjectOutputStream out;
	private ObjectInputStream in;
	
	public ClientConnection(Socket socket) throws IOException
	{
		this.socket = socket;
		out = new ObjectOutputStream(socket.getOutputStream());
		in = new ObjectInputStream(socket.getInputStream());
	}
	
	public void write(Object obj) throws IOException
	{
		out.reset();
		out.writeUnshared(obj);
	}
	
	public Object read() throws ClassNotFoundException, IOException
	{
		return in.readUnshared();
	}
	
	public ObjectOutputStream getOut()
	{
		return out;
	}
	
	public ObjectInputStream getIn()
	{
		return in;
	}
	
	public void setTimeout(int time) throws SocketException
	{
		socket.setSoTimeout(time);
	}
	
	public void sendPlayer(Player player) throws IOException
	{
		write("update.player");
		write(player);
	}
	
	public void sendEnemy(Enemy enemy) throws IOException
	{
		write("update.enemy");
		write(enemy);
	}
	
	public void close()
	{
		try
		{
			socket.close();
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}
}