package ar.com.trips.persistencia.dao.impl;

import java.util.List;

import org.hibernate.Session;
import org.springframework.transaction.annotation.Transactional;

import ar.com.trips.persistencia.dao.IAtraccionDAO;
import ar.com.trips.persistencia.modelo.Atraccion;

public class AtraccionDAOImpl extends DAOImpl implements IAtraccionDAO {

	@Override
	public List<Atraccion> listarPorCiudad(Long idCiudad) {
		Session session = sessionFactory.openSession();
		String query = "FROM " + Atraccion.class.getName() + " a WHERE a.ciudad.id = " + idCiudad + " AND a.borrado = 0";
		@SuppressWarnings("unchecked")
		List<Atraccion> lista = session.createQuery(query).list();
		session.close();
		return lista;
	}

	@Transactional
	public void borrar(Long id) {
		Session s = sessionFactory.openSession();
		s.beginTransaction();
		Atraccion model = (Atraccion) s.get(Atraccion.class, id);
		model.setBorrado(1);
		s.update(model);
		s.getTransaction().commit();
		s.close();
	}

	@Override
	public boolean atraccionExistente(Atraccion atraccion) {
		Session session = sessionFactory.openSession();
		String query = "FROM " + Atraccion.class.getName() + " a WHERE a.nombre = '" + atraccion.getNombre() + "'"
								+ " AND a.ciudad.id = '" + atraccion.getCiudad().getId() + "' AND a.borrado = 0 "
								+ " AND a.id != '" + atraccion.getId() + "'";
		@SuppressWarnings("unchecked")
		List<Atraccion> lista = session.createQuery(query).list();
		session.close();
		return lista.size() != 0;
	}

	@Override
	public Atraccion get(Long id) {
		return this.get(Atraccion.class, id);
	}
}