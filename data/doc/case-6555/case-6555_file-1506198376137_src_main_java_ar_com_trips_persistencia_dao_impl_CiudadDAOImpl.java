package ar.com.trips.persistencia.dao.impl;

import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;

import ar.com.trips.persistencia.dao.ICiudadDAO;
import ar.com.trips.persistencia.modelo.Ciudad;

public class CiudadDAOImpl extends DAOImpl implements ICiudadDAO {

	@Autowired
	protected SessionFactory sessionFactoryAux;
	
	@Override
	public boolean ciudadExistente(Ciudad ciudadModelo) {
		Session session = sessionFactoryAux.openSession();
		String query = "FROM " + Ciudad.class.getName() + " c WHERE c.nombre = '" + ciudadModelo.getNombre() + "'"
						+ " AND c.pais = '" + ciudadModelo.getPais() + "'";
		@SuppressWarnings("unchecked")
		List<Ciudad> lista = session.createQuery(query).list();
		session.close();
		return lista.size() != 0;
	}
	
	@Transactional
	public void borrar(long id) {
		Session s = sessionFactoryAux.openSession();
		s.beginTransaction();
		Ciudad model = (Ciudad) s.get(Ciudad.class, id);
		model.setBorrado(1);
		s.update(model);
		s.getTransaction().commit();
		s.close();
	}

	@Override
	public Ciudad get(Long id) {
		return this.get(Ciudad.class, id);
	}
}